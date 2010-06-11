class LCD
  def initialize value = nil
    @number = value
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
