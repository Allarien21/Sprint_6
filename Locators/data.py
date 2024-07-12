from Locators.transition_locator import Transition

order_data = [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "ул. Пушкина, д. 1",
            "metro_station": "Пушкинская",
            "phone": "+79991234567",
            "date": "12.12.2024",
            "period": "сутки",
            "color": "black",
            "comment": "Позвонить за час до доставки",
        },
        {
            "name": "Петр",
            "surname": "Петров",
            "address": "ул. Лермонтова, д. 5",
            "metro_station": "Лермонтовский проспект",
            "phone": "+79998765432",
            "date": "13.12.2024",
            "period": "двое суток",
            "color": "grey",
            "comment": "Оставить у двери",
        }
    ]

transition_data = [
    (Transition.QUESTION_ONE, Transition.ANSWER_ONE, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (Transition.QUESTION_TWO, Transition.ANSWER_TWO, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (Transition.QUESTION_THREE, Transition.ANSWER_THREE, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (Transition.QUESTION_FOUR, Transition.ANSWER_FOUR, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (Transition.QUESTION_FIVE, Transition.ANSWER_FIVE, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (Transition.QUESTION_SIX, Transition.ANSWER_SIX, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (Transition.QUESTION_SEVEN, Transition.ANSWER_SEVEN, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (Transition.QUESTION_EIGHT, Transition.ANSWER_EIGHT, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
]