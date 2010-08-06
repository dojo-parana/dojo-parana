def fizzbuzz(s,e)
  l = []
  for i in s..e
    v = ""
    if i%3 == 0
      v += "fizz"
    end
    if i%5 == 0
      v += "buzz"
    end
    l << v
  end
  return l
end
