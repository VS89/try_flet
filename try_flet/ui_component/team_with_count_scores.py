import flet as ft


class TeamWithCountScores(ft.UserControl):
    """
    Класс для описания UI количества голов команды
    """

    def __init__(self, home_team_flag=False, away_team_flag=False):
        super().__init__()
        self.txt_number_score = ft.TextField(value="0", width=50, height=40, read_only=True)
        self.home_team_flag = home_team_flag
        self.away_team_flag = away_team_flag

    def build(self):

        liv_img = ft.Image(
            src="https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/1200px-Liverpool_FC.svg.png",
            # src="try_flet/images/Liverpool_FC.svg.png",
            width=100,
            height=100,
            border_radius=ft.border_radius.all(10)
        )

        city_img = ft.Image(
            src="https://upload.wikimedia.org/wikipedia/ru/thumb/9/96/"
                "Manchester_City_FC.svg/1200px-Manchester_City_FC.svg.png",
            # src="./images/Manchester_City_FC.svg.png",
            width=100,
            height=100,
            border_radius=ft.border_radius.all(10)
        )

        if self.home_team_flag:
            return ft.Row(
                width=175,
                controls=[
                    ft.Column(controls=[liv_img]),
                    ft.Column(controls=[
                        ft.Row(controls=[ft.IconButton(ft.icons.ADD, on_click=self.plus_click)]),
                        ft.Row(controls=[self.txt_number_score]),
                        ft.Row(controls=[ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click)]),
                    ])
                ]
            )
        elif self.away_team_flag:
            return ft.Row(
                width=300,
                controls=[
                    ft.Column(controls=[
                        ft.Row(controls=[ft.IconButton(ft.icons.ADD, on_click=self.plus_click)]),
                        ft.Row(controls=[self.txt_number_score]),
                        ft.Row(controls=[ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click)]),
                    ]),
                    ft.Column(controls=[city_img])
                ]
            )

    async def plus_click(self, e):
        if int(self.txt_number_score.value) <= 8:
            self.txt_number_score.value = str(int(self.txt_number_score.value) + 1)
        else:
            error_dialog = ft.AlertDialog(title=ft.Text("Давай оставаться в пределах разумного"))
            self.page.dialog = error_dialog
            error_dialog.open = True
        await self.update_async()

    async def minus_click(self, e):
        if int(self.txt_number_score.value) >= 1:
            self.txt_number_score.value = str(int(self.txt_number_score.value) - 1)
        else:
            error_dialog = ft.AlertDialog(title=ft.Text("Счет не может быть отрицательным"))
            self.page.dialog = error_dialog
            error_dialog.open = True
        await self.update_async()
