class Romano
  def initialize numero
    @numero = numero
  end

  def to_roman
    if @numero > 5
      return "V" + "I"*(@numero-5)
    end 

    case @numero
      when 1..3
      	"I"*@numero
      when 4
        "IV"
      when 5
        "V"
      when 6
        "VI"
      when 7
        "VII"
    end    
  end
end
