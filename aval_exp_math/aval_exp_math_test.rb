require "test/unit"
require "aval_exp_math"

class AvalExpMathTest < Test::Unit::TestCase
  def test_create_aval_exp_math
    aval=AvalExpMath.new
    assert_equal(aval.sum, 2)
    
  end
end
