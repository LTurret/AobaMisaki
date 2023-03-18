import json

from discord.ext import commands

with open("./config/scope.json") as server_scopes:
    server_scopes = json.load(server_scopes)
    GUILD_ID = server_scopes["GUILD_ID"]
    CHANNEL_ID = server_scopes["CHANNEL_ID"]

class general(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    async def tantou(self, ctx, idol_name: str, role_id: int, testing: bool=False):

        guild = self.Misaki.get_guild(GUILD_ID)
        member = guild.get_member(ctx.author.id)
        role = guild.get_role(role_id)

        isForceId = {
            True:  CHANNEL_ID,
            False: ctx.channel.id
        }
        isForceId = isForceId[testing]

        if not any(list(map(lambda x: x.name == f"{idol_name}P", member.roles))) and isForceId == CHANNEL_ID:
            await member.add_roles(role)
            await ctx.send(f"**{idol_name}**擔當增加成功！")

        elif any(list(map(lambda x: x.name == f"{idol_name}P", member.roles))) and isForceId == CHANNEL_ID:
            await member.remove_roles(role)
            await ctx.send(f"**{idol_name}**擔當移除成功！")

    @commands.command()
    async def 春香P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "春香", 961206505158373407, isForceId)

    @commands.command()
    async def 千早P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "千早", 960940329001943041, isForceId)

    @commands.command()
    async def 美希P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "美希", 961301052483850350, isForceId)

    @commands.command()
    async def 雪步P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "雪步", 961301109866106961, isForceId)

    @commands.command()
    async def 彌生P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "彌生", 961302204151636039, isForceId)

    @commands.command()
    async def 真P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "真", 961302498394648577, isForceId)

    @commands.command()
    async def 伊織P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "伊織", 961302677281730560, isForceId)

    @commands.command()
    async def 貴音P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "貴音", 961305734539259984, isForceId)

    @commands.command()
    async def 律子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "律子", 961305841997320274, isForceId)

    @commands.command()
    async def 梓P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "梓", 961306042619285584, isForceId)

    @commands.command()
    async def 亞美P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "亞美", 961307022119280680, isForceId)

    @commands.command()
    async def 真美P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "真美", 961307055464009798, isForceId)

    @commands.command()
    async def 響P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "響", 961307089328832583, isForceId)

    @commands.command()
    async def 未來P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "未來", 961308003540303924, isForceId)

    @commands.command()
    async def 靜香P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "靜香", 961308006820233257, isForceId)

    @commands.command()
    async def 翼P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "翼", 961308010351841320, isForceId)

    @commands.command()
    async def 琴葉P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "琴葉", 961308013736624218, isForceId)

    @commands.command()
    async def 艾琳娜P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "艾琳娜", 961308017285025863, isForceId)

    @commands.command()
    async def 美奈子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "美奈子", 961308021395447828, isForceId)

    @commands.command()
    async def 恵美P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "恵美", 961308024293716049, isForceId)

    @commands.command()
    async def 茉莉P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "茉莉", 961309675180142592, isForceId)

    @commands.command()
    async def 星梨花P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "星梨花", 961309765038899241, isForceId)

    @commands.command()
    async def 茜P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "茜", 961309779748327514, isForceId)

    @commands.command()
    async def 杏奈P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "杏奈", 960949894590390313, isForceId)

    @commands.command()
    async def RocoP(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "Roco", 961309792540966943, isForceId)

    @commands.command()
    async def 百合子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "百合子", 961309796013850674, isForceId)

    @commands.command()
    async def 紗代子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "紗代子", 961309799365115924, isForceId)

    @commands.command()
    async def 亞利沙P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "亞利沙", 961309802678616164, isForceId)

    @commands.command()
    async def 海美P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "海美", 961309805962752010, isForceId)

    @commands.command()
    async def 育P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "育", 961310136826220545, isForceId)

    @commands.command()
    async def 朋花P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "朋花", 961315450183123054, isForceId)

    @commands.command()
    async def EmilyP(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "Emily", 961316146831822988, isForceId)

    @commands.command()
    async def 志保P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "志保", 961040774475157594, isForceId)

    @commands.command()
    async def 步P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "步", 961316151663685652, isForceId)

    @commands.command()
    async def 日向P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "日向", 961316154050232391, isForceId)

    @commands.command()
    async def 可奈P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "可奈", 961316154838753321, isForceId)

    @commands.command()
    async def 奈緒P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "奈緒", 961316152938733630, isForceId)

    @commands.command()
    async def 千鶴P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "千鶴", 961316156277395466, isForceId)

    @commands.command()
    async def 木實P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "木實", 961304315346186370, isForceId)

    @commands.command()
    async def 環P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "環", 961316155774095462, isForceId)

    @commands.command()
    async def 風花P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "千鶴", 961316157716066375, isForceId)

    @commands.command()
    async def 美也P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "木實", 961316158710116442, isForceId)

    @commands.command()
    async def 法子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "環", 961316157250494485, isForceId)

    @commands.command()
    async def 瑞希P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "瑞希", 961319945893986374, isForceId)

    @commands.command()
    async def 可憐P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "可憐", 961319989309214730, isForceId)

    @commands.command()
    async def 莉緒P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "莉緒", 961320014277935104, isForceId)

    @commands.command()
    async def 昴P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "昴", 961320043071832084, isForceId)

    @commands.command()
    async def 麗花P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "麗花", 961320067965009980, isForceId)

    @commands.command()
    async def 桃子P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "桃子", 961320094514937907, isForceId)

    @commands.command()
    async def 茱莉亞P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "茱莉亞", 961041043938242570, isForceId)

    @commands.command()
    async def 紬P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "紬", 961320134318895234, isForceId)

    @commands.command()
    async def 歌織P(self, ctx, isForceId:bool=False):
        await self.tantou(ctx, "歌織", 961320170809339915, isForceId)

async def setup(Misaki):
    await Misaki.add_cog(general(Misaki))