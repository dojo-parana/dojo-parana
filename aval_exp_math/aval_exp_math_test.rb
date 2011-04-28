require "test/unit"
require "aval_exp_math"

class aval_exp_mathTest < Test::Unit::TestCase
  def test_create_aval_exp_math
    assert_not_nil(aval_exp_math.new)
  end
end