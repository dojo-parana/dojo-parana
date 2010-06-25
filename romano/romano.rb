class Fixnum
 
  def to_roman
    case self
      when 1..3
      	"I"*self
      when 4
        "IV"
      when 5..8
        "V" + "I"*(self-5)
      when 9
        "IX"
      when 10..13
        "X" + "I"*(self-10)
      when 14
        "XIV"
      when 20
        "XX"
    end
  end
end
