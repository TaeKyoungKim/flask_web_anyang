#hashcode 바꾸는 기능
from passlib.hash import pbkdf2_sha256

#회원가입 기능 구현할때 쓰기위한 테스트
hash = pbkdf2_sha256.hash("toomanysecrets")

# print(hash)
#로그인 기능 구현할때 쓰기 위해 테스트
result = pbkdf2_sha256.verify("tfewfwefoomanysecrets",hash)
print(result)