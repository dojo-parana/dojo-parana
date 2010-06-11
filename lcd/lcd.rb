class LCD
  def initialize value = nil
    @number = value
  end

  def self.make_digit leds
    if leds[0] == 0
       retorno = "    \n"
    elsif leds[0] == 1
        retorno = " -- \n"
    end
    if leds[1] == 0
        retorno += "    \n    \n"
    elsif leds[1] == 1
        retorno += "|   \n|   \n"
    end
    return retorno
  end

  def to_s
    if @number==0
        " -- \n|  |\n|  |\n    \n|  |\n|  |\n -- \n"
    elsif @number==1
        "    \n   |\n   |\n    \n   |\n   |\n    \n"
    elsif @number==2
        " -- \n   |\n   |\n -- \n|   \n|   \n -- \n"
    end
  end
end
