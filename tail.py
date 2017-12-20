import subprocess
def tail(f, n):
  cmd = "tail -n "+str(n)+" "+str(f);
  # stdstdin,stdout = subprocess.popen2(cmd)

  print(cmd)
  p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
  stdin, stdout = (p.stdin, p.stdout)

  stdin.close()
  lines = stdout.readlines(); stdout.close()
  return lines[-n]


last_line = tail("Recordings/BTC-XRP_December_19.csv", 1)
# last_line = tail("BTC-XRP_Monday_18_Dec.csv", 1)
print(last_line)
