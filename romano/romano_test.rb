require "test/unit"
require "romano"

class RomanoTest < Test::Unit::TestCase
  def test_numero_1
    assert_equal(Romano.new(1).to_roman, "I")
  end

  def test_numero_2
    assert_equal(Romano.new(2).to_roman, "II")
  end
end
