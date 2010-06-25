class Romano
  def initialize numero
    @numero = numero
  end

  def to_roman

    case @numero
      when 1..3
      	"I"*@numero
      when 4
        "IV"
      when 5..8
        "V" + "I"*(@numero-5)
      when 9
        "IX"
      when 10
        "X"
      when 11
        "XI"
      when 20
        "XX"
    end
  end
end
