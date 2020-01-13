import datetime
import hashlib

def hash(password):
  return hashlib.sha256(password.encode())
  
def salted_hash(password_hash, deltatime=datetime.timedelta(seconds=0)):
  time = datetime.datetime.now() - deltatime
  salted_password_hash = '%i-%i-%i-%s-%i-%i-%i' % (time.year, time.month, time.day,
                                                   password_hash.hexdigest(),
                                                   time.hour, time.minute, time.second)
  return hashlib.sha256(salted_password_hash.encode()).hexdigest()

def accepted_salted_hashes(password_hash):
  return [salted_hash(password_hash),
          salted_hash(password_hash, datetime.timedelta(seconds=1))]
