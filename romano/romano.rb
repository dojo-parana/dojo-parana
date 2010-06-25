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
    end    
  end
end
