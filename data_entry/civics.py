import re
from playwright.sync_api import Playwright, sync_playwright
from funcCivics import *
import time

def login(page):
    page.goto("https://www.measuringuplive.com/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("stullyrl")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Password1!")
    page.get_by_role("button", name="LOG IN").click()


def createQuestion(page):
    print_reference = input("Enter print reference\n")
    difficulty_level = input("Enter difficulty level 1-5\n")
    state_difficulty = input("State difficulty level (E,A,D)\n")
    RBT = input("Enter RBT (Remember, Understand, Apply, Analyze, Create, Evaluate) \n")
    BKD = input("Enter Blooms Knowledge Dimension (F,C,P,M)\n")
    WDK = input("Enter Depth on knowledge level (1,2,3,4)\n")

    page.get_by_label("Content linkPress enter or").click()
    page.get_by_label("Question Search linkPress").click()
    page.get_by_title("Create Question").locator("span").click()
    page.locator(".button-image").first.click()
    page.locator("#standardSetId-input").select_option("34")
    page.locator("#gradeLevelId-input").select_option("7")
    page.locator("#masterSubjectId-input").select_option("19")
    page.get_by_text("Go").click()
    page.locator("#standard-body-2b2656b8-7682-4633-8207-49c5941b5720 label").first.click()
    page.locator("#create-question-nav-tab-1 div").nth(1).click()
    page.locator("input[type=\"text\"]").click()
    div_locator = "body > div.me-container.common-bg > div.container > section > div > div > div.tab-holder.create-question-tab-holder > div > div > div.general-header.panel-collapse.collapse.in > div:nth-child(2) > div.question-id > div.question-id-text"
    div_text = page.locator(div_locator).inner_text()
    print(f'Question ID: {div_text}')
    page.locator("input[type=\"text\"]").fill(print_reference)
    #difficulty levels
    page.locator("#difficultyLevels-input").select_option(str(DLdict[difficulty_level]))
    #state difficulty levels
    if state_difficulty.lower() == "e":
        state_difficulty = "E - Easy"
    elif state_difficulty.lower() == "a":
        state_difficulty = "A - Average"
    elif state_difficulty.lower() == "d":
        state_difficulty = "D - Difficult"

    page.get_by_text(state_difficulty).click()
    #revised blooms taxonomy
    page.locator("#blooms-input").select_option(RBTdic[RBT])
    #blooms knowledge dimension
    page.locator("#RevisedBlooms-input").select_option(BKDdict[BKD.upper()])
    #Webbs Depth of knowledge
    page.locator("#Wook-input").select_option(WDKdict[str(WDK)])
    page.locator("#create-question-nav-tab-3").click()
    page.locator(".authoring-template-container").click()
    page.get_by_text("Multiple Choice/Multiple").click()
    page.get_by_text("Next").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor1\"]").get_by_text("Enter question").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor1\"]").locator("body").fill("question stem")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor2\"]").get_by_text("Enter answer option").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor2\"]").locator("body").fill("answer a")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor3\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor3\"]").locator("body").fill("answer b")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor4\"]").get_by_text("Enter answer option").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor4\"]").locator("body").fill("answer c")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor5\"]").get_by_text("Enter answer option").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor5\"]").locator("body").fill("answer d")
    page.get_by_role("radio").first.check()
    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(2).check()
    page.locator("div:nth-child(4) > .row-container > .row-selection-container").click()
    page.locator("#tab-holder").get_by_text("Next").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor6\"]").locator("body").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor6\"]").locator("body").fill("cue a")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor7\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor7\"]").locator("body").fill("cue b")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor8\"]").get_by_text("Enter answer cue").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor8\"]").locator("body").fill("cue c")
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor9\"]").get_by_text("Enter answer cue").click()
    page.frame_locator("iframe[title=\"Rich Text Editor\\, editor9\"]").locator("body").fill("cue d")
    page.locator("#tab-holder").get_by_text("Done").click()
    #page.get_by_text("Yes", exact=True).click()



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login(page)  # Call the login function
    createQuestion(page)  # Call the create question function
    while True:
        # Wait for user input to continue or break the loop
        user_input = input("run again? Y or N:\n")
        if user_input.lower() != 'y':
            break
        elif user_input.lower() == 'y':
            createQuestion(page)


    browser.close()



with sync_playwright() as playwright:
    run(playwright)
