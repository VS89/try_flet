import flet as ft

from try_flet.ui_component.team_with_count_scores import TeamWithCountScores


async def main(page: ft.Page):

    page.title = 'First async app'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    await page.update_async()

    team_home = TeamWithCountScores(home_team_flag=True)
    team_away = TeamWithCountScores(away_team_flag=True)
    await page.add_async(ft.Row(controls=[team_home, team_away]))


if __name__ == '__main__':
    ft.app(main, port=8550, view=ft.WEB_BROWSER)
