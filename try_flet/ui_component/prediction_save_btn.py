import flet as ft


class PredictionSaveBtn(ft.UserControl):
    """
    Класс для описания кнопки сохранения прогнозов
    """

    # TODO для демо подойдет, но нужно точно отрефачить и сделать по нормальному
    def __init__(self, all_controls):
        super().__init__()
        self.save_btn = ft.ElevatedButton('Save prediction', on_click=self.button_clicked)
        self.txt_success = ft.Text()
        self.all_controls = all_controls

    def build(self):
        return ft.Row(controls=[ft.Column(controls=[ft.Row(controls=[self.save_btn]),
                                                    ft.Row(controls=[self.txt_success])])])

    async def button_clicked(self, e):
        # TODO доставать таким образом счета для 10 мачтей будет пздц
        team_home_score = self.all_controls[0].txt_number_score.value
        team_away_score = self.all_controls[1].txt_number_score.value
        self.txt_success.value = f"Save predictions:\n" \
                                 f"LIV: {team_home_score} - {team_away_score} MNC"
        await self.update_async()


