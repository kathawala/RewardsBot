xpath = { 'signInLink': "//div[contains(@class, 'msame_unauth')]",
          'usernameBox': ".//*[@id='i0116']",
          'pswdBox': ".//*[@id='i0118']",
          'submit': ".//*[@id='idSIButton9']", #needs to be clicked after username input and after password input
          'rewardsBox': ".//*[@id='id_rc']",
          'search': ".//*[@id='sb_form_q']",
          'searchButton': ".//*[@id='sb_form_go']",
          'searchButtonMobile': ".//*[@id='sbBtn']",

          # Find a better, more portable way to describe this xpath
          'searchLink': "//*[@id='offer-evergreen_ENUS_search_level2_PC_JAN18']",
          'searchLinkMobile': "//*[@id='offer-evergreen_ENUS_search_level2_Mobile_JAN18']",
          'startQuizButton': "//*[@id='rqStartQuiz']",
          'draggableQuizBox': "//*[@id='dragOptionContainer']",
          'allDragAnswers': "//*[contains(@class, 'rqDragOption')]",
          'wrongDragAnswers': "//*[contains(@class, 'wrongDragAnswer')]",
          'rightDragAnswers': "//*[contains(@class, 'correctDragAnswer')]",
          'quizOption0': "//*[@id='rqAnswerOption0']",
          'quizOption1': "//*[@id='rqAnswerOption1']",
          'quizOption2': "//*[@id='rqAnswerOption2']",
          'quizOption3': "//*[@id='rqAnswerOption3']",

          # Scrub all the elements which aren't visible using
          # https://stackoverflow.com/questions/19669786/check-if-element-is-visible-in-dom
          # Then, the Titles and NextToCheckmarks should be 1-to-1
          # (i.e. T[0] corresponds to NTC[0])
          'rewardsHomeCardTitle': "//div[contains(@class, 'offer-card')]/div/div[contains(@class, 'card-padding')]/div[contains(@class, 'offer-title-height')]",
          'rewardsHomeCardPoints': "//*[contains(@class, 'card-button-line-height') and contains(@class, 'margin-right-15')]",
          'rewardsHomeCardCheckmarkOrChevron': "//div[contains(@class, 'offer-card-button-background')]/span/span[contains(@class, 'card-button-line-height') and contains(@class, 'margin-right-15')]/following-sibling::span"
         }