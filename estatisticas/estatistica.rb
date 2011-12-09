#!/usr/bin/env ruby
#
# automatically created by Dojo Polyglot Environ on 2011-12-09 19:54:15
# https://github.com/afurlan/dojo-polyglot-environ

require "test/unit"

class Estatistica
   
    attr_accessor :vetor

    def initialize
      @vetor = []
    end

    def add_vetor(elementos)
        elementos.each do |i| @vetor.push(i)
        end 
    end

    def add_elemento(elemento)
        @vetor.push(elemento)
    end
    def menor
        min = @vetor[0]
        @vetor.each do |i| 
            if i < min 
                min = i
            end
        end 
        return min
    end
    def maior
        max = @vetor[0]
        @vetor.each do |i| 
            if i > max 
                max = i
            end
        end 
        return max
    end
    def media
        med = 0.0
        @vetor.each do |i| 
            med = med + i 
        end 
        return med.fdiv(@vetor.length)
    end

end

class Testestatistica < Test::Unit::TestCase
    def test_initialize
        assert_not_nil(Estatistica.new)
    end
    def test_vetor_deve_iniciar_vazia
        estatistica = Estatistica.new
        assert(estatistica.vetor.empty?)
    end
    def test_vetor1_dever_retornar1
        estatistica = Estatistica.new
        estatistica.add_elemento(1)
        assert_equal(estatistica.vetor.length,1)    
    end
    def test_vetor2_deve_retornar2
        estatistica = Estatistica.new
        estatistica.add_elemento(1)
        estatistica.add_elemento(1)
        assert_equal(estatistica.vetor.length,2)
    end
    def test_inicializar_com_vetor
        estatistica = Estatistica.new
        estatistica.add_vetor([1,2,3])
        assert_equal(estatistica.vetor.length, 3)
    end
    def test_menor_de_3_elementos
        estatistica = Estatistica.new
        estatistica.add_vetor([2,1,3])
        assert_equal(estatistica.menor, 1)
    end    
    def test_maior_de_3_elementos
        estatistica = Estatistica.new
        estatistica.add_vetor([2,1,3])
        assert_equal(estatistica.maior, 3)
    end    
    def test_media
        estatistica = Estatistica.new
        estatistica.add_vetor([2,1,3])
        assert_equal(estatistica.media, 2)
    end    
    def test_media_decimal
        estatistica = Estatistica.new
        estatistica.add_vetor([2,1,3,9])
        assert_equal(estatistica.media, 3.75)
    end    
        
end

