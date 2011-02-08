require "test/unit"

class Telefone
  attr_accessor :file, :content
  def initialize
    @file = File.open('/home/dojo/sandbox/dojo-parana/telefone/arquivo.txt', 'r')
    @content = @file.read
  end
  
    def processar_caracter s
        dicionario = {"A" => "2", "B" => "2", "C" => "2", 
                      "D" => "3", "E" => "3", "F" => "3", 
                      "G" => "4", "H" => "4", "I" => "4",
                      "J" => "5", "K" => "5", "L" => "5", 
                      "M" => "6", "N" => "6", "O" => "6", 
                      "P" => "7", "Q" => "7", "R" => "7", "S" => "7", 
                      "T" => "8", "U" => "8", "V" => "8",
                      "W" => "9", "X" => "9", "Y" => "9", "Z" => "9",
                      "1" => "1", "0" => "0",} 
                      
        dicionario[s]
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
    assert_equal(Telefone.new.processar_caracter("A"), "2")
  end
  
  def test_substituicao_c
    assert_equal(Telefone.new.processar_caracter("C"), "2")
  end
  
  def test_substituicao_d
    assert_equal(Telefone.new.processar_caracter("D"), "3")
  end
  
  def test_substituicao_e
    assert_equal(Telefone.new.processar_caracter("E"), "3")
  end
  def test_substituicao_w
    assert_equal(Telefone.new.processar_caracter("W"), "9")
  end
end
