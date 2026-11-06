/**
 * Centralized API & Server Gateway Configuration
 * Enables seamless communication between Android APK (Capacitor/WebView) and the Cloud Backend Server
 * Also manages client-side Google Gemini API Key for direct offline/standalone AI access
 */

// Official Production/Cloud Run API Server Endpoints
export const DEFAULT_CLOUD_API_URL = 'https://ais-pre-g5w3wggai6dcyye22rmjnk-772838390153.asia-southeast1.run.app';
export const DEV_CLOUD_API_URL = 'https://ais-dev-g5w3wggai6dcyye22rmjnk-772838390153.asia-southeast1.run.app';

const STORAGE_GATEWAY_KEY = 'pydroid_api_gateway_url';
const STORAGE_GEMINI_KEY = 'pydroid_gemini_api_key';

/**
 * Checks if a string looks like a Google Gemini API Key rather than a URL
 */
export function isLikelyGeminiApiKey(str: string): boolean {
  if (!str) return false;
  const trimmed = str.trim();
  // Google API keys typically start with AIzaSy and are 39 chars, or alphanumeric ~35-45 chars without http/slashes
  return (
    trimmed.startsWith('AIza') ||
    (!trimmed.includes('/') && !trimmed.includes(':') && trimmed.length >= 25 && trimmed.length <= 60)
  );
}

/**
 * Checks if the current environment is running inside an Android APK (Capacitor / native wrapper)
 * or local offline file/localhost context.
 */
export function isAndroidApkEnvironment(): boolean {
  if (typeof window === 'undefined') return false;
  const isCapacitor = !!(window as any).Capacitor;
  const origin = window.location.origin || '';
  const host = window.location.hostname || '';
  const protocol = window.location.protocol || '';

  return (
    isCapacitor ||
    origin.startsWith('capacitor://') ||
    origin.startsWith('http://localhost') ||
    origin.startsWith('https://localhost') ||
    protocol === 'file:' ||
    (host === 'localhost' && window.location.port !== '3000')
  );
}

/**
 * Returns the active API Gateway Base URL.
 * - When in Web browser on Cloud Run: returns empty string "" (relative paths /api/* work automatically)
 * - When in Android APK or overridden by user: returns configured cloud URL
 * - Auto-heals if user previously pasted an API key into the URL field!
 */
export function getApiBaseUrl(): string {
  if (typeof window === 'undefined') return '';

  const saved = localStorage.getItem(STORAGE_GATEWAY_KEY);
  if (saved && saved.trim()) {
    const clean = saved.trim().replace(/\/+$/, '');

    // Auto-heal: If user previously pasted an API key (AIza...) into the Server URL field:
    if (isLikelyGeminiApiKey(clean)) {
      console.warn('[API Gateway] Detected Gemini API Key stored in Server URL field. Auto-migrating to Gemini Key storage.');
      setGeminiApiKey(clean);
      localStorage.removeItem(STORAGE_GATEWAY_KEY);
      return DEFAULT_CLOUD_API_URL;
    }

    if (clean.startsWith('http://') || clean.startsWith('https://')) {
      return clean;
    }
  }

  // If running inside APK or offline wrapper, auto-connect to live cloud server
  if (isAndroidApkEnvironment()) {
    return DEFAULT_CLOUD_API_URL;
  }

  // In standard web mode, relative path is optimal
  return '';
}

/**
 * Returns the effective API base URL for display purposes (even when in relative mode)
 */
export function getDisplayApiBaseUrl(): string {
  const current = getApiBaseUrl();
  if (current) return current;
  if (typeof window !== 'undefined' && window.location.origin && window.location.origin !== 'null') {
    return window.location.origin;
  }
  return DEFAULT_CLOUD_API_URL;
}

/**
 * Persists a custom API Gateway URL (or reset to default)
 */
export function setApiBaseUrl(url: string): void {
  if (typeof window === 'undefined') return;
  const clean = url.trim().replace(/\/+$/, '');

  // If user pasted a Gemini Key into the URL field, automatically save to Gemini key instead!
  if (isLikelyGeminiApiKey(clean)) {
    setGeminiApiKey(clean);
    return;
  }

  if (clean && (clean.startsWith('http://') || clean.startsWith('https://'))) {
    localStorage.setItem(STORAGE_GATEWAY_KEY, clean);
  } else {
    localStorage.removeItem(STORAGE_GATEWAY_KEY);
  }
}

/**
 * Retrieves the user-provided Google Gemini API Key (if any)
 */
export function getGeminiApiKey(): string {
  if (typeof window === 'undefined') return '';
  return (localStorage.getItem(STORAGE_GEMINI_KEY) || '').trim();
}

/**
 * Persists or clears the user-provided Google Gemini API Key
 */
export function setGeminiApiKey(key: string): void {
  if (typeof window === 'undefined') return;
  const clean = key.trim();
  if (clean) {
    localStorage.setItem(STORAGE_GEMINI_KEY, clean);
  } else {
    localStorage.removeItem(STORAGE_GEMINI_KEY);
  }
}

/**
 * Returns common HTTP headers for API calls, including the custom Gemini key if available
 */
export function getApiHeaders(extraHeaders: Record<string, string> = {}): Record<string, string> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...extraHeaders,
  };
  const key = getGeminiApiKey();
  if (key) {
    headers['x-gemini-api-key'] = key;
  }
  return headers;
}

/**
 * Constructs a full API URL for any endpoint (e.g. '/api/ai/chat')
 */
export function getApiUrl(path: string): string {
  const base = getApiBaseUrl();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  if (!base) return normalizedPath;
  return `${base}${normalizedPath}`;
}

/**
 * Constructs a WebSocket URL matching the active API Gateway
 */
export function getWebSocketUrl(path: string): string {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const base = getApiBaseUrl();

  if (base) {
    // Convert https://... to wss://... or http://... to ws://...
    const wsBase = base.replace(/^https:\/\//i, 'wss://').replace(/^http:\/\//i, 'ws://');
    return `${wsBase}${normalizedPath}`;
  }

  if (typeof window !== 'undefined' && window.location.host) {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    return `${protocol}//${window.location.host}${normalizedPath}`;
  }

  return `wss://localhost${normalizedPath}`;
}

/**
 * Tests connection to the Cloud API Gateway (/api/system/status)
 */
export async function testApiGatewayConnection(customUrl?: string): Promise<{
  ok: boolean;
  latencyMs: number;
  message: string;
  details?: any;
}> {
  const targetBase = customUrl !== undefined
    ? customUrl.trim().replace(/\/+$/, '')
    : getApiBaseUrl();

  const testUrl = targetBase
    ? `${targetBase}/api/system/status`
    : '/api/system/status';

  const startTime = performance.now();
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 8000);

    const resp = await fetch(testUrl, {
      method: 'GET',
      signal: controller.signal,
      headers: {
        'Accept': 'application/json',
      },
    });
    clearTimeout(timeout);

    const latencyMs = Math.round(performance.now() - startTime);
    if (!resp.ok) {
      return {
        ok: false,
        latencyMs,
        message: `Máy chủ phản hồi mã lỗi HTTP ${resp.status}`,
      };
    }

    const data = await resp.json();
    return {
      ok: true,
      latencyMs,
      message: 'Kết nối Cổng Cloud Backend thành công! CPython, Pip và AI sẵn sàng.',
      details: data,
    };
  } catch (err: any) {
    const latencyMs = Math.round(performance.now() - startTime);
    return {
      ok: false,
      latencyMs,
      message: err.name === 'AbortError'
        ? 'Quá thời gian chờ phản hồi (timeout sau 8s)'
        : (err.message || 'Không thể kết nối đến máy chủ'),
    };
  }
}

/**
 * Validates a Gemini API Key directly against Google's Gemini API
 * Supports modern models (gemini-3.8-flash, gemini-flash-latest, gemini-3.1-flash-lite)
 * Automatically handles model compatibility (e.g. gemini-2.5 upgrade notification)
 */
export async function testGeminiApiKeyDirectly(apiKey: string): Promise<{
  ok: boolean;
  message: string;
  modelUsed?: string;
}> {
  const cleanKey = apiKey.trim();
  if (!cleanKey) {
    return { ok: false, message: 'Vui lòng nhập khóa API Gemini' };
  }

  // Model fallback chain: Gemini 3.8 Flash -> Gemini Flash Latest -> Gemini 3.1 Flash Lite
  const models = ['gemini-3.8-flash', 'gemini-flash-latest', 'gemini-3.1-flash-lite', 'gemini-2.5-flash'];

  let lastError = '';

  for (const model of models) {
    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 9000);

      const resp = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(cleanKey)}`,
        {
          method: 'POST',
          signal: controller.signal,
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            contents: [
              {
                parts: [{ text: 'Hello, respond with OK' }],
              },
            ],
            generationConfig: {
              maxOutputTokens: 10,
            },
          }),
        }
      );
      clearTimeout(timeout);

      if (resp.ok) {
        return {
          ok: true,
          message: `Khóa API Gemini hợp lệ & hoạt động xuất sắc với model [${model}]!`,
          modelUsed: model,
        };
      }

      const errData = await resp.json().catch(() => ({}));
      const errMsg = errData.error?.message || `HTTP ${resp.status}`;

      // If error says model not found / not supported, continue to next model
      if (
        errMsg.toLowerCase().includes('not found') ||
        errMsg.toLowerCase().includes('not supported') ||
        errMsg.toLowerCase().includes('unsupported')
      ) {
        lastError = errMsg;
        continue;
      }

      // If permission or invalid key error, fail immediately
      return {
        ok: false,
        message: `Google Gemini từ chối khóa: ${errMsg}`,
      };
    } catch (e: any) {
      lastError = e.message || 'Lỗi kết nối';
    }
  }

  return {
    ok: false,
    message: `Không thể xác thực khóa: ${lastError || 'Vui lòng kiểm tra lại khóa API và kết nối mạng'}`,
  };
}
