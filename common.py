import datetime
import hashlib

def salted_hash(password):
  password_hash = hashlib.sha256(password.encode())
  current_time = datetime.datetime.now()
  salted_password_hash = '%i-%i-%i-%s-%i-%i-%i' % (current_time.year, current_time.month, current_time.day,
                                                  password_hash.hexdigest(),
                                                  current_time.hour, current_time.minute, current_time.second)
  return salted_password_hash
  #return hashlib.sha256(salted_password_hash.encode()).hexdigest()