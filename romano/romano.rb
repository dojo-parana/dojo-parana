class Romano
  def initialize numero
    @numero = numero
  end

  def to_roman
    if @numero == 1
      "I"
    elsif @numero == 2
      "II"
    elsif @numero == 3
      "III"
    end
    
  end
end
