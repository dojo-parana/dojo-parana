require "test/unit"
require "romano"

class RomanoTest < Test::Unit::TestCase
  def test_numero_1
    assert_equal(Romano.new(1).to_roman, "I")
  end

  def test_numero_2
    assert_equal(Romano.new(2).to_roman, "II")
  end

  def test_numero_3
    assert_equal(Romano.new(3).to_roman, "III")
  end

  def test_numero_4
    assert_equal(Romano.new(4).to_roman, "IV")
  end

  def test_numero_5
    assert_equal(Romano.new(5).to_roman, "V")
  end

  def test_numero_6
    assert_equal(Romano.new(6).to_roman, "VI")
  end

  def test_numero_7
    assert_equal(Romano.new(7).to_roman, "VII")
  end

  def test_numero_8
    assert_equal(Romano.new(8).to_roman, "VIII")
  end

  def test_numero_9
    assert_equal(Romano.new(9).to_roman, "IX")
  end

  def test_numero_10
    assert_equal(Romano.new(10).to_roman, "X")
  end

  def test_numero_11
    assert_equal(Romano.new(11).to_roman, "XI")
  end

  def test_numero_13
    assert_equal(Romano.new(13).to_roman, "XIII")
  end
  
  def test_numero_20
    assert_equal(Romano.new(20).to_roman, "XX")
  end

end
