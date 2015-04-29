from splinter import Browser
import uuid
import time

def main():
    suffix = '%s@mailinator.com'

    for i in range(0,100):
        e = suffix % uuid.uuid1().int.__str__()[0:8]
        browser = Browser()
        check_inbox(vote(browser,e),e)
        print 'Email criado:' + e


def vote(browser,email,vote_url='http://telavivamovel.com.br/entretenimento/'):
    browser.visit(vote_url)
    browser.choose('votonaopcao', '1')
    browser.fill('email',email)
    browser.find_by_id('votar').first.click() 
    return browser

def check_inbox(browser,email,inbox_url='https://mailinator.com/index.jsp'):    
    browser.visit(inbox_url)
    g = browser.find_by_id('inboxfield')
    g.fill(email)
    time.sleep(5)
    check = browser.find_by_css('.btn-success')
    check.click()
    inbox = browser.find_by_id('mailcontainer')
    all = inbox.find_by_css('.from')
        
    for email in all:
        if 'Oi TVM' in email.value:
            email.click()
    
    time.sleep(5)
    with browser.get_iframe('rendermail') as iframe:
        iframe.click_link_by_partial_href('http://www.telavivamovel.com.br/premio')
    browser.quit()

def confirm_vote(browser):
    with browser.get_iframe('rendermail') as iframe:
        iframe.click_link_by_partial_href('http://www.telavivamovel.com.br/premio')



if __name__ == "__main__":
    main()
