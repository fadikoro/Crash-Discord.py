# # # # # # # # # # #
#                   #
#  osmuzov was here #
#  Сломанный Краш   #
#                   #
# # # # # # # # # # #

# импорты
import discord
from discord.ext import commands
import math
import random

@commands.command()
async def crash(self, ctx, bet: int = None, coef: int = None):
    if bet is None:
        await ctx.send(f"{ctx.author.name}, Укажи сумму!")

    elif coef is None:
        await ctx.send(f"{ctx.author.name}, Укажи коэффициент!")

    elif coef <= 1:
        await ctx.send(f"{ctx.author.name}, Коэффициент должен быть выше 1x!")

    else:
        cash = #баланс участника из базы данных
        if cash < bet:
            await ctx.send(f"{ctx.author.name}, У тебя недостаточно денег!")

        else:
            # ограничение по беттингу (10/100000)
            if bet < 10:
                await ctx.send("Минимальная ставка 10 монет!")
            elif bet > 100000:
                await ctx.send("Максимальная ставка 100000 монет!")

            else:
                #Для генерации результата в режиме Crash требуется 1 случайное число в интервале (0..1), 
                #которое затем переводится в коэффициент Crash, имеющий экспоненциальное распределение,
                #по следующему алгоритму.
                number = random.uniform(0, 1)
                crashOutcome = 1000000 / (math.floor(number * 1000000) + 1) * (1 - 0.05)

                #Иногда может выпасть число по типу 0.99 или меньше, в самой игре такого нет,
                #этот IF спасает от таких ситуации.
                if crashOutcome <= 1:
                    crashOutcome = 1.00
            
                #если коэф пользователя выше или равен крашу, то он выиграл
                if crashOutcome >= coef:
                    winCash = bet * coef - bet
                    roundWinCash = round(winCash)
                    await ctx.send(content= ctx.author.mention, embed = discord.Embed(title="📈 Сломанный Краш", description=f"{ctx.author.name}, ты выиграл: **+{round(roundwincash)} :dollar:**\n\nКоэф: **{round(crashmultipler, 2)}**\nТы поставил на коэф: **{round(xmult,2)}**\nТвоя ставка: **{bet}**"))

                    #Тут уже входит в силу ваша ваза данных.
                    #переменная roundWinCash, это выигрыш пользователя.

                #или проиграл :(
                else:
                    await ctx.send(content= ctx.author.mention, embed = discord.Embed(title="📈 Сломанный Краш", description=f"{ctx.author.name}, ты проиграл: **{bet} :dollar:**\n\nКоэф: **{round(crashmultipler, 2)}**\nТы поставил на коэф: **{round(xmult,2)}**\nТвоя ставка: **{bet}**"))

                    #Тут уже входит в силу ваша ваза данных.
                    #тут вы должны снять с баланса пользователя его ставку
