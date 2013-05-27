#!/usr/bin/env ruby
#
# automatically created by Dojo Polyglot Environ on 2013-05-27 19:35:46
# https://github.com/afurlan/dojo-polyglot-environ

require "test/unit"

class Miojo
    def initialize
    end

    def preparo(cozimento, ampulheta1, ampulheta2)
        #if cozimento == ampulheta1
        #    return ampulheta1
        #end
        #if cozimento == ampulheta2
        #    return ampulheta2
        #end

        if cozimento % 2 == 1 && ampulheta1 % 2 == 0 && ampulheta2 % 2 == 0
            return -1
        end
        
        if cozimento % ampulheta1 == 0
            return cozimento
        end
        
        if cozimento % ampulheta2 == 0
            return cozimento
        end
        
        if cozimento == (ampulheta1 - ampulheta2).abs
            return [ampulheta1,ampulheta2].max
        end

        10
    end
end

class TestMiojo < Test::Unit::TestCase
    def test_initialize
        assert_not_nil(Miojo.new)
    end

    def test_default
        miojo = Miojo.new
        tempo = miojo.preparo(3, 5, 7)
        assert_equal(10, tempo)
    end

    def test_caso_trivial
       miojo = Miojo.new
       tempo = miojo.preparo(3, 3, 5)
       assert_equal(3, tempo)
    end

    def test_caso_naotrivial
       miojo = Miojo.new
       tempo = miojo.preparo(5, 3, 5)
       assert_equal(5, tempo)
    end

    def test_duas_ampulhetas_7
       miojo = Miojo.new
       tempo = miojo.preparo(7, 7, 7)
       assert_equal(7, tempo)
    end

    def test_cozimento_14_2_ampulheta_7
       miojo = Miojo.new
       tempo = miojo.preparo(14, 7, 7)
       assert_equal(14, tempo)
    end

    def test_cozimento_14_com_ampulheta_3_e_outra_7
       miojo = Miojo.new
       tempo = miojo.preparo(14, 3, 7)
       assert_equal(14, tempo)
    end				

    def test_cozimento_de_3_com_amplulhetas_impares
        miojo = Miojo.new
        tempo = miojo.preparo(3, 2, 2)
        assert_equal(-1, tempo)
    end

    def test_cozimento_e_diferencia_entre_ampulhetas
        miojo = Miojo.new
        tempo = miojo.preparo(2, 3, 5)
        assert_equal(5, tempo)
    end

    def test_cozimento_e_diferencia_entre_ampulhetas_invertido
        miojo = Miojo.new
        tempo = miojo.preparo(2, 5, 3)
        assert_equal(5, tempo)
    end

end
