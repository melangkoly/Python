# __init__.py
# 패키지 임포트할 때 초기화 작업을 수행하는 파일
# 요새는 없어도 패키지로 인식함
from mysqlite.database import *

# from 패키지 import * : 내부에 있는 모든 객체를 임폿
__all__ = ["Database"] # 명시된 데이터베이스만 Export 된다
#__all__ = [] # *로 임포트할 때 암것도 export 안함