#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   test.py                                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 15:19:57 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 15:19:57 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from recipe import Recipe
from book import Book


if __name__ == '__main__':
    tourte = Recipe('Tourte', 2, 70, ['pate', 'lardons'], "Etape1.", 'lunch')
    to_print = str(tourte)
    book = Book('ok', '2019-12-01', '2018-02-14',
                {"starter": [tourte], "lunch": [], "dessert": []})
    book.get_recipe_by_name('Tourte')
