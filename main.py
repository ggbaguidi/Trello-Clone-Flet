"""Entry point of app"""
import flet
from flet import ( Page, Text, SafeArea, colors )


if __name__ == '__main__':
    def main(page: Page):
        """main function"""
        page.title = "Trello Clone Flet"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        page.add(SafeArea(Text("Hello, Flet!")))
        page.update()


    flet.app(target=main, view=flet.WEB_BROWSER)
