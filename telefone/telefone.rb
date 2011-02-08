require "test/unit"

class Telefone
  attr_accessor :file
  def initialize
    @file = File.open('/home/dojo/sandbox/dojo-parana/telefone/arquivo.txt', 'r')
  end
end

class TelefoneTest < Test::Unit::TestCase
  def test_create_telefone
    assert_not_nil(Telefone.new)
  end
  
  def teste_open_file
    assert_equal(File === Telefone.new.file, true)
  end
end
