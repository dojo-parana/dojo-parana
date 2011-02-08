require "test/unit"

class Telefone
  attr_accessor :file, :content
  def initialize
    @file = File.open('/home/dojo/sandbox/dojo-parana/telefone/arquivo.txt', 'r')
    @content = @file.read
  end
  
    def processar_linha s
        "2"
    end 
end

class TelefoneTest < Test::Unit::TestCase
  def test_create_telefone
    assert_not_nil(Telefone.new)
  end
  
  def teste_open_file
    assert_equal(File === Telefone.new.file, true)
  end
  
  def test_read_file
    assert_not_nil(Telefone.new.content)
  end
  
  def test_content_not_empty
    assert_not_equal(Telefone.new.content, "")
  end
  
  def test_substituicao
    assert_equal(Telefone.new.processar_linha("A"), "2")
  end
end
