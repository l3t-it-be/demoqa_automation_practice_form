from selene import browser, have, be, command

from tests.conftest import path


def test_automation_form():
    browser.open('/')

    browser.should(have.title('DEMOQA'))
    browser.all('h1')[0].should(have.exact_text('Practice Form'))
    browser.all('h5')[0].should(have.exact_text('Student Registration Form'))

    # WHEN
    browser.element('#firstName').should(be.blank).type('Yasha')
    browser.element('#lastName').should(be.blank).type('Kramarenko')
    browser.element('#userEmail').should(be.blank).type('yashaka@gmail.com')
    browser.element('[name=gender][value=Male]+label').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1986')
    browser.element('.react-datepicker__month-select').type('September')
    browser.all('.react-datepicker__week')[4].element(
        '.react-datepicker__day--030'
    ).click()

    browser.element('#subjectsInput').type('maths').press_enter()
    browser.element('#subjectsInput').type('arts').press_enter()
    browser.element('#subjectsInput').type('computer science').press_enter()
    browser.element('#subjectsInput').type('english').press_enter()
    browser.element('#subjectsInput').type('social studies').press_enter()

    browser.element('#hobbiesWrapper').element('[for=hobbies-checkbox-3]').click()

    browser.element('#uploadPicture').send_keys(path('yasha.jpg'))

    browser.element('#currentAddress').should(be.blank).type('K-PAX')

    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # THEN
    browser.element('.modal-header').should(
        have.exact_text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Yasha Kramarenko',
            'yashaka@gmail.com',
            'Male',
            '1234567890',
            '30 September,1986',
            'Maths, Arts, Computer Science, English, Social Studies',
            'Music',
            'yasha.jpg',
            'K-PAX',
            'NCR Delhi',
        )
    )
