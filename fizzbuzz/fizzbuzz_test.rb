require "test/unit"
require "fizzbuzz"

class FizzbuzzTest < Test::Unit::TestCase
  def test_create_fizzbuzz
    assert_not_nil(Fizzbuzz.new)
  end
end