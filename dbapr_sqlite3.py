# 모듈 임포트
import sqlite3, os
from sqlite3 import Error

# 접속 (Access)
def create_connection(db_file):
    # ./database 디렉터리 생성
    if not os.path.exists("./database"): # 현재 디렉터리 아래 database 디렉터리가 없으면
        os.makedirs("./database") # 생성해라

    # 접속
    try:
        conn = sqlite3.connect(db_file) # connection 객체 반환
        print(sqlite3.version) #
    except Error as e:
        print(e, type(e))
        return None # 접속 실패시 None 반환
    return conn

# 파라미터 이용 INSERT
def test_insert_data(db_file, name, category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    # 익명 파라미터 바인딩
    sql = """INSERT INTO customer(name, category, region)
        Values(?, ?, ?)"""
    res = conn.execute(sql, (name, category, region))

    # INSERT or UPDATE or DELETE -> 영향 받은 레코드의 수.rowcount로 리턴
    print("{}개의 레코드가 영향을 받음".format(res.rowcount))
    conn.commit()
    conn.close()

def test_delete_all(db_file):
    conn = create_connection(db_file)
    sql = "DELETE FROM customer"
    res = conn.execute(sql)

    print("{} 개의 레코드가 삭제됨".format(res.rowcount))
    conn.commit()
    conn.close()

def test_insert_bulk_data(db_file):
    # 테스트 데이터 여러개 insert
    test_delete_all(db_file)
    test_insert_data(db_file, "둘리", 1, "부천")
    test_insert_data(db_file, "고길동", 2, "서울")
    test_insert_data(db_file, "이찬우", 3, "서울")
    test_insert_data(db_file, "홍길동", 4, "서울")
    test_insert_data(db_file, "이수민", 5, "부산")

def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()

def test_create_table(db_file):
    # 접속
    conn = create_connection(db_file) # Connection
    # 커서 획득
    cursor = conn.cursor() # Cursor
    # sql 작성
    ddl = """CREATE TABLE IF NOT EXISTS
    customer(
        id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))
    """
    # sql 실행
    cursor.execute(ddl)
    # 접속 해제
    conn.close()


if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    #test_connection(db_file)
    #test_create_table(db_file)
    #test_insert_data(db_file, "둘리", 1, "부천")
    test_insert_bulk_data(db_file)