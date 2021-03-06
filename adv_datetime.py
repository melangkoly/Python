# datetime module
# datetime Class
# date Class
# time Class
import datetime # 모듈 임포트

def get_datetime():
    # 시간의 획득 : 현재 날짜와 시간
    now = datetime.datetime.now()
    print(now)

    # 생성자 이용, 직접 날짜를 정할 수 있다
    dt = datetime.datetime(1999, 12, 31) # 최소 년 월 일은 지정
    print(dt)

    # datetime의 주요 속성들
    print("date 관련 속성 : ", dt.year, dt.month, dt.day)
    print("time 관련 속성 : ", dt.hour, dt.minute, dt.second, dt.microsecond)

    # 요일 확인 : weekday 월 : 0 ~ 일 : 6
    print("오늘은 무슨 요일 ? " , now.weekday())

    # datetime 객체는 date 객체 + time 객체
    print(now.date(), type(now.date())) # 날짜 관련 속성 을 가진 date 객체
    print(now.time(), type(now.time())) # 시간 관련 속성을 가진 time 객체

    # date 객체는 datetime 클래스의 날짜 관련 속성과 요일 메소드 이용
    # time 객체는 datetime 클래스의 시간 관련 속성 이용
    nowdate = datetime.datetime.now().date()
    nowtime = datetime.datetime.now().time()
    print("date : ", nowdate.year, nowdate.month, nowdate.day, nowdate.weekday())
    print("time : ", nowtime.hour, nowtime.minute, nowtime.second, nowtime.microsecond)

def timedelta_ex():
    """
    timedelta : 두 datetime 사이의 간격 정보 객체
    """
    current = datetime.datetime.now()
    print("CURRENT : ", current)
    past = datetime.datetime(1999, 12, 31)
    print("PAST :", past)
    # 두 datetime은 대소 비교가 가능하지
    print("CURRENT가 PAST보다 이후? ", current > past)

    # datetime - datetime = timedelta (간격값)
    diff = current - past
    print(diff, type(diff))

    # timedelta의 속성
    print("timedelta : ", diff.days, diff.seconds, diff.microseconds)
    print("total seconds : ", diff.total_seconds()) #   모든 속성을 초단위로 모아서 반환

    # datetime + datetime  : New datetime
    # 현재 시간에서 100일 후 정보
    print("Current : ", current)
    diff = datetime.timedelta(100, 0, 0)
    print("100일 후 : ", current + diff)

def format_date():
    """
    문자열 포맷
        datetime ->str : .strftime()
        str -> datetime : .strptime()
    """
    current = datetime.datetime.now()
    print("Current : ", current)

    # datetime -> str
    print(current.strftime("%Y-%m-%d %H:%M"))
    print(current.strftime("%Y년 %m월 %d일 %H시 %M분"))

    # str -> datetime : strptime()
    s = "2021 - 05 - 24 17 : 00 : 00"
    dt = datetime.datetime.strptime(s, # 변환할 문자열
                                        "%Y-%m-%d %H:%M:%S" )
    print(dt,type(dt))

if __name__ == "__main__":
    #get_datetime()
    #timedelta_ex()
    format_date()