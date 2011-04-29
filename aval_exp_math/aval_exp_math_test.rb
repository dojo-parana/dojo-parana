require "test/unit"
require "aval_exp_math"

class AvalExpMathTest < Test::Unit::TestCase

  def test_1plus1
    aval=AvalExpMath.new("1 + 1")
    assert_equal(aval.solve_exp, 2)
    
  end

  def test_5minus2
    aval = AvalExpMath.new("5 - 2")
    assert_equal(aval.solve_exp, 3)  
  end

  def test_first_char
    aval = AvalExpMath.new("5")
    assert_equal(aval.solve_exp, "5")      
  end

  def test_operador
    aval = AvalExpMath.new("5 *")
    assert_equal(aval.solve_exp, "*")      
  end

  def test_multi
    aval = AvalExpMath.new("5 * 2")
    assert_equal(aval.solve_exp, 10)      
  end

end
