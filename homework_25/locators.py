https://qauto2.forstudy.space

# XPath locators
home_navigation = //div[@class="header_left d-flex align-items-center"]//a[@class="btn header-link -active" and text()="Home"]
Sign_In_button = //div[@class="header_right d-flex align-items-center"]/button[@class="btn btn-outline-white header_signin" and text()="Sign In"]
Guest log in  - //button[@class="header-link -guest" and text()="Guest log in"]
instagram - //div[@id="contactsSection"]//a//span[@class="socials_icon icon icon-instagram"]
suport - //div[@id="contactsSection"]//a[@class="contacts_link h4"]
about - //div[@class="header_left d-flex align-items-center"]//button[@class="btn header-link" and @appscrollto="aboutSection"]
contactsSection - //div[@class="header_left d-flex align-items-center"]//button[@class="btn header-link" and @appscrollto="contactsSection"]
2021... - //app-footer//p[text()="© 2021 Hillel IT school"]
ithillel - //div[@id="contactsSection"]//a[@class="contacts_link display-4"]
Contacts - //div[@id="contactsSection"]//h2[text()="Contacts"]
Sign up - //div[@class="app-content"]//button[@class="hero-descriptor_btn btn btn-primary"]
FB - //div[@id="contactsSection"]//div[@class="contacts_socials socials"]//a//span[@class="socials_icon icon icon-telegram"]
Instructions and manuals - //div[@class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"]//div[@class="about-block"]//p[@class="about-block_title h2"]
about-block_picture about-picture - //div[@id="aboutSection"]//div[@class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"]//img[@alt="Instructions"]


#click on sign-in button
email field - //ngb-modal-window//input[@id="signinEmail"]
forgot password - //ngb-modal-window//div[@class="form-group d-flex align-items-center justify-content-between"]//button[@class="btn btn-link" and text()="Forgot password"]
remember me - //ngb-modal-window//label[@class="form-check-label" and normalize-space()="Remember me"]
registration - //ngb-modal-window//div[@class="modal-footer d-flex justify-content-between"]//button[@class="btn btn-link" and text()="Registration"]
login - //ngb-modal-window//div[@class="modal-content"]//button[@class="btn btn-primary"]
close - //ngb-modal-window//div[@class="modal-content"]//button[@class="close"]
password -//ngb-modal-window//div[@class="modal-body"]//input[@id="signinPassword"]

#sign-in > forgot password:
email - //ngb-modal-window[@class="d-block modal fade show"]//div[@class="form-group"]//input[@id="signinEmail"]
send - //ngb-modal-window[@class="d-block modal fade show"]//div[@class="modal-footer"]//button[@class="btn btn-primary" and text()="Send"]
x - //ngb-modal-window[@class="d-block modal fade show"]//div[@class="modal-content"]//button[@class="close"]

#https://qauto2.forstudy.space/panel/garage
addcar - //div[@class="app-content"]//div[@class="panel-page_heading d-flex justify-content-between"]//button[@class="btn btn-primary" and text()="Add car"]
log out -//div[@class="app-content"]//div[@class="col-3 d-none d-lg-block sidebar-wrapper"]//a/span[@class="icon icon-logout"]
instractions - //div[@class="app-content"]//div[@class="col-3 d-none d-lg-block sidebar-wrapper"]//a[@routerlink="instructions"]

________________________
# css
home_navigation = div.header_left.d-flex.align-items-center a.btn.header-link.-active
Sign_In_button = div.header_right.d-flex.align-items-center button.btn.btn-outline-white.header_signin
Guest log in button.header-link.-guest
instagram - div#contactsSection a span.socials_icon.icon.icon-instagram
suport - div#contactsSection a.contacts_link.h4
about - div.header_left.d-flex.align-items-center button.btn.header-link[appscrollto="aboutSection"]
contactsSection - div.header_left.d-flex.align-items-center button.btn.header-link[appscrollto="contactsSection"]
ithillel - div#contactsSection a.contacts_link.display-4
Sign up - div.app-content button.hero-descriptor_btn.btn.btn-primary
FB - div#contactsSection div.contacts_socials.socials a span.socials_icon.icon.icon-telegram
Instructions and manuals - div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 div.about-block p.about-block_title.h2
about-block_picture about-picture - div#aboutSection div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 img[alt="Instructions"]


#click on sign-in button
email field - ngb-modal-window input#signinEmail
forgot password - ngb-modal-window div.form-group.d-flex.align-items-center.justify-content-between button.btn.btn-link
remember me- ngb-modal-window label.form-check-label
registration - ngb-modal-window div.modal-footer.d-flex.justify-content-between button.btn.btn-link
login - ngb-modal-window div.modal-content button.btn.btn-primary
close - ngb-modal-window div.modal-content button.close
password - ngb-modal-window div.modal-body input#signinPassword


#sign-in > forgot password:
email - ngb-modal-window.d-block.modal.fade.show div.form-group input#signinEmail
send - ngb-modal-window.d-block.modal.fade.show div.modal-footer button.btn.btn-primary
x - ngb-modal-window.d-block.modal.fade.show div.modal-content button.close

#https://qauto2.forstudy.space/panel/garage
addcar - div.app-content div.panel-page_heading.d-flex.justify-content-between button.btn.btn-primary
log out -div.app-content div.col-3.d-none.d-lg-block.sidebar-wrapper a span.icon.icon-logout
instractions -div.app-content div.col-3.d-none.d-lg-block.sidebar-wrapper a[routerlink="instructions"]




