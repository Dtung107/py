import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock


class GameQuaySo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.danh_sach_mua = []
        self.is_quay = False
        self.so_hien_tai = '00'
        self.dem_lap = 0
        self.ket_qua_final = '00'

        # Tiêu đề
        self.add_widget(Label(
            text='🎰 CHƯƠNG TRÌNH QUAY SỐ 2 CHỮ SỐ 🎰',
            font_size='22sp',
            bold=True,
            color=(1, 1, 0, 1),
            size_hint_y=None,
            height=45
        ))

        # Khu vực hiển thị số đang quay
        self.label_quay = Label(
            text='00',
            font_size='52sp',
            bold=True,
            color=(0.2, 0.8, 0.2, 1),
            size_hint_y=None,
            height=70
        )
        self.add_widget(self.label_quay)

        # Ô nhập số
        self.add_widget(Label(
            text='Mời nhập số cần mua (00 - 99):',
            font_size='18sp',
            size_hint_y=None,
            height=30
        ))

        self.input_so = TextInput(
            multiline=False,
            input_filter='int',
            font_size='24sp',
            halign='center',
            size_hint_y=None,
            height=50,
            maxlength=2
        )
        self.add_widget(self.input_so)

        # Các nút chức năng
        self.layout_nut = BoxLayout(size_hint_y=None, height=55, spacing=10)
        btn_them = Button(text='Thêm Số', background_color=(0.2, 0.6, 1, 1), font_size='16sp')
        btn_them.bind(on_press=self.them_so)
        self.layout_nut.add_widget(btn_them)

        btn_quay = Button(text='Quay Số', background_color=(0.2, 0.8, 0.2, 1), font_size='16sp')
        btn_quay.bind(on_press=self.quay_so)
        self.layout_nut.add_widget(btn_quay)

        btn_xoa = Button(text='Xóa Danh Sách', background_color=(0.8, 0.2, 0.2, 1), font_size='16sp')
        btn_xoa.bind(on_press=self.xoa_danh_sach)
        self.layout_nut.add_widget(btn_xoa)

        self.add_widget(self.layout_nut)

        # Khu vực thông báo
        self.label_thong_bao = Label(
            text='Danh sách số bạn đang có: []',
            font_size='16sp',
            halign='center',
            valign='top',
            size_hint_y=None
        )
        self.label_thong_bao.bind(texture_size=self._cap_nhat_kich_thuoc_label)

        self.scroll = ScrollView(do_scroll_x=False)
        self.scroll.add_widget(self.label_thong_bao)
        self.add_widget(self.scroll)

    def _cap_nhat_kich_thuoc_label(self, instance, size):
        instance.height = max(size[1], 100)

    def _sua_lai_label(self, text):
        self.label_thong_bao.text = text
        self.label_thong_bao.texture_update()
        self.label_thong_bao.height = self.label_thong_bao.texture_size[1]

    def _normalize_so(self, text):
        text = (text or '').strip()
        if not text:
            return ''
        if text.isdigit():
            if len(text) == 1:
                return text.zfill(2)
            if len(text) == 2:
                return text
        return ''

    def them_so(self, instance):
        if self.is_quay:
            self._sua_lai_label('⚠️ Đang quay số, vui lòng chờ kết quả...')
            return

        mua_so = self._normalize_so(self.input_so.text)

        if not mua_so:
            self._sua_lai_label('❌ Lỗi: Bạn phải nhập số có 2 chữ số (00-99)!')
            self.input_so.text = ''
            return

        if mua_so in self.danh_sach_mua:
            self._sua_lai_label(f'⚠️ Số {mua_so} đã có trong danh sách rồi!')
            self.input_so.text = ''
            return

        self.danh_sach_mua.append(mua_so)
        self._sua_lai_label(
            f'✅ Đã lưu số: {mua_so}\n\n'
            f'Danh sách số bạn đang có:\n'
            f'{", ".join(self.danh_sach_mua)}'
        )
        self.input_so.text = ''

    def xoa_danh_sach(self, instance):
        self.danh_sach_mua = []
        self._sua_lai_label('🧹 Đã xóa toàn bộ danh sách số.')
        self.input_so.text = ''
        self.label_quay.text = '00'

    def quay_so(self, instance):
        if self.is_quay:
            return

        if not self.danh_sach_mua:
            self._sua_lai_label('❌ Bạn chưa mua số nào cả! Hãy chọn ít nhất 1 số trước khi quay.')
            return

        self.is_quay = True
        self.dem_lap = 0
        self.ket_qua_final = str(random.randint(0, 99)).zfill(2)

        Clock.schedule_interval(self._quay_hieu_ung, 0.08)

    def _quay_hieu_ung(self, dt):
        self.dem_lap += 1
        self.so_hien_tai = str(random.randint(0, 99)).zfill(2)
        self.label_quay.text = self.so_hien_tai

        if self.dem_lap >= 22:
            Clock.unschedule(self._quay_hieu_ung)
            self.label_quay.text = self.ket_qua_final

            chuoi = f'🎰 KẾT QUẢ QUAY SỐ: ==> {self.ket_qua_final} <==\n\n'
            chuoi += f'Danh sách số bạn đã mua: {", ".join(self.danh_sach_mua)}\n\n'

            if self.ket_qua_final in self.danh_sach_mua:
                chuoi += '🎉 CHÚC MỪNG! Bạn đã trúng số rồi! 🎉'
            else:
                chuoi += '😭 Rất tiếc, bạn không trúng lần này. Chúc bạn may mắn lần sau!'

            self._sua_lai_label(chuoi)
            self.danh_sach_mua = []
            self.is_quay = False
            self.input_so.text = ''


class MainApp(App):
    def build(self):
        self.title = 'Game Quay Số Kivy'
        return GameQuaySo()


if __name__ == '__main__':
    MainApp().run()
