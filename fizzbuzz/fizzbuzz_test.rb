require "test/unit"
require "fizzbuzz"

class FizzbuzzTest < Test::Unit::TestCase
  def test_0_eh_fizzbuzz
    assert_equal(fizzbuzz(0,100)[0], "fizzbuzz")
  end

  def test_3_eh_fizz
    assert_equal(fizzbuzz(0,100)[3], "fizz")
  end

  def test_5_eh_buzz
    assert_equal(fizzbuzz(0,100)[5], "buzz")
  end
end
