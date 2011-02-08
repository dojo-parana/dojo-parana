require "test/unit"

class Telefone
  def initialize
    File.open('/home/dojo/sandbox/dojo-parana/telefone/arquivo.txt', 'r')
  end
end

class TelefoneTest < Test::Unit::TestCase
  def test_create_telefone
    assert_not_nil(Telefone.new)
  end
  
  def teste_open_file
    assert_not_nil(Telefone.new)
  end
end
