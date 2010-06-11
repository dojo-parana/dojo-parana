require "test/unit"
require "lcd"

class LCDTest < Test::Unit::TestCase
  def test_create_lcd
    assert_not_nil(LCD.new)
  end

  def test_um_caracter_0
    assert_equal(LCD.new(0).to_s," -- \n|  |\n|  |\n    \n|  |\n|  |\n -- \n")
  end
  def test_um_caracter_1
    assert_equal(LCD.new(1).to_s,"   |\n   |\n   |\n    \n   |\n   |\n   |\n")
  end

  
end
