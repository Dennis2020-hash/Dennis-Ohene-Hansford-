def donuts(count):
    if count >10:
        print("Number of donuts: Many")
    else:
        print("Number of donuts: {}" .format(count))
print
donuts(9)


def both_end(s):
    if len(s)<2:
        print ((''))
    else:
        print(s[0:2]+s[-2:])
        
both_end ("spritual")


def fix_start(s):
    back = s[1:]
    sp= back.replace(s[0],'*')
    return(s[0]+sp)

print(fix_start('daddy'))


def mix_up(a,b):
    return (b[:2] + a[2:] + '' + a[:2] +b[2:])

print (mix_up ('dog','dinner'))


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

    
# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print ('both_end')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
