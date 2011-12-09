#!/usr/bin/env ruby
#
# automatically created by Dojo Polyglot Environ on 2011-12-09 19:54:15
# https://github.com/afurlan/dojo-polyglot-environ

require "test/unit"

class Estatistica
   
    attr_accessor :vetor

    def initialize
      @vetor = nil
    end

    def add_vetor(elemento)
        @vetor = [elemento]
    end
end

class Testestatistica < Test::Unit::TestCase
    def test_initialize
        assert_not_nil(Estatistica.new)
    end
    def test_vetor_deve_iniciar_vazia
        estatistica = Estatistica.new
        assert_nil(estatistica.vetor)
    end
    def test_vetor1_dever_retornar1
        estatistica = Estatistica.new
        estatistica.add_vetor(1)
        assert_equal(estatistica.vetor.length,1)    
    end
        
end

