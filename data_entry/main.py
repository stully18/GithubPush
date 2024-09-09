import re
from playwright.sync_api import Playwright, sync_playwright, expect


def login(page):
    page.goto("https://www.measuringuplive2.com/")
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("stullyrl")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Password1!")
    page.get_by_role("button", name="LOG IN").click()

# Function to create a question
def create_question(page):
    page.get_by_label("Content linkPress enter or").click()
    page.get_by_label("Question Search linkPress").click()
    page.get_by_text("Create Question").click()
    page.locator(".button-image").first.click()
    page.locator("#standardSetId-input").select_option("31")
    page.locator("#gradeLevelId-input").select_option("10")
    page.locator("#masterSubjectId-input").select_option("3")
    page.get_by_text("Go").click()
    page.locator(".primary-radio-holder > .cfa").first.click()
    page.locator("#create-question-nav-tab-1 div").nth(1).click()
    page.locator("input[type=\"text\"]").click()
    div_locator = "body > div.me-container.common-bg > div.container > section > div > div > div.tab-holder.create-question-tab-holder > div > div > div.general-header.panel-collapse.collapse.in > div:nth-child(2) > div.question-id > div.question-id-text"
    div_text = page.locator(div_locator).inner_text()
    print(f'Question ID: {div_text}')
    print_reference = input("Enter print reference\n")
    page.locator("input[type=\"text\"]").fill(print_reference)
    page.locator("label").filter(has_text="Answer Eliminator").locator("div").first.click()
    page.locator("#difficultyLevels-input").select_option('1')
    page.locator("#blooms-input").select_option('Remember')
    page.locator("#RevisedBlooms-input").select_option('F - Factual')
    page.locator("#Wook-input").select_option('Level 1 - Recall')
    page.locator("#create-question-nav-tab-2 div").nth(1).click()
    page.locator("#standardSetId-input").select_option("31")
    page.locator("#subject-input").select_option("ELA")
    page.get_by_placeholder("Search by title or description").click()
    page.get_by_placeholder("Search by title or description").fill("television")
    page.locator("#go-button-container div").click()

# Main function to control the workflow
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    while True:
        login(page)  # Call the login function
        create_question(page)  # Call the create question function

        # Wait for user input to continue or break the loop
        user_input = input("run again? Y or N:\n")
        if user_input.lower() != 'y':
            break

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
