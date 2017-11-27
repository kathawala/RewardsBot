xpath = { 'signInLink': "//div[contains(@class, 'msame_unauth')]",
          'usernameBox': ".//*[@id='i0116']",
          'pswdBox': ".//*[@id='i0118']",
          'submit': ".//*[@id='idSIButton9']", #needs to be clicked after username input and after password input
          'rewardsBox': ".//*[@id='id_rc']",
          'search': ".//*[@id='sb_form_q']",
          'searchButton': ".//*[@id='sb_form_go']",
          'searchButtonMobile': ".//*[@id='sbBtn']",

          # For these the month and year needs to be set at runtime
          'searchLink': "//*[@id='offer-evergreen_ENUS_search_level2_PC_NOV17']",
          'searchLinkMobile': "//*[@id='offer-evergreen_ENUS_search_level2_Mobile_NOV17']",
          'startQuizButton': "//*[@id='rqStartQuiz']"
         }


css = {
    'rewardsHomeCard': ".offer-card",
    'rewardsHomeTitle': "div.offer-card>div>div.card-padding>div.offer-title-height",
    'rewardsHomeDesc': "div.offer-card>div>div.card-padding>div.offer-description-height",
    # Already done marker (if you find this under parent, it's already done)
    'rewardsHomeCardDone': ".win-icon-CheckMark",


    'searchLink': "#offer-evergreen_ENUS_search_level2_PC_NOV17",
    'searchLinkMobile': ".offer-evergreen_ENUS_search_level2_Mobile_NOV17"
}