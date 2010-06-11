require "test/unit"
require "lcd"

class LCDTest < Test::Unit::TestCase
  def test_create_lcd
    assert_not_nil(LCD.new)
  end

  #def test_um_caracter_0
#    assert_equal(LCD.new(0).to_s," -- \n|  |\n|  |\n    \n|  |\n|  |\n -- \n")
  #end
  #def test_um_caracter_1
  #  assert_equal(LCD.new(1).to_s,"    \n   |\n   |\n    \n   |\n   |\n    \n")
#  end
#  def test_um_caracter_2
#    assert_equal(LCD.new(2).to_s," -- \n   |\n   |\n -- \n|   \n|   \n -- \n")
#  end

    def test_seg_topo
      assert(LCD.make_digit([1, 0, 0, 0, 0, 0, 0]).start_with?(" -- \n"))
    end
    def test_seg_topo_off
      assert(LCD.make_digit([0, 0, 0, 0, 0, 0, 0]).start_with?("    \n"))
    end

    def test_seg_esq1
        s = LCD.make_digit([1, 1, 0, 0, 0, 0, 0]).lines.to_a   
        assert(s[1].start_with?("|"))
        assert(s[2].start_with?("|"))
    end

    def test_seg_esq1_off
        s = LCD.make_digit([0, 0, 0, 0, 0, 0, 0]).lines.to_a   
        assert(s[1].start_with?(" "))
        assert(s[2].start_with?(" "))
    end
  
end
