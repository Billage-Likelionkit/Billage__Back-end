def message(domain, uidb64, token):
    text = """
        <html>
        <p>아래 링크를 클릭하면 회원가입 인증이 완료됩니다.</p>
        <a href="http://{domain}/accounts/activate/{uidb64}/{token}">메일 인증받기</a>
        </html>
    """
    text = text.replace('{domain}', str(domain))
    text = text.replace('{uidb64}', str(uidb64))
    text = text.replace('{token}', str(token))
    print(text)
    return text
