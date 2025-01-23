from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
import random

from .models import LuckyNumber

admin.site.site_title = "TicketsPlus site admin (DEV)"
admin.site.site_header = "TicketsPlus administration"
admin.site.index_title = "Site administration"

class LuckyNumberAdmin(admin.ModelAdmin):
    #list_display = ('nome', 'numero_da_sorte', 'origem')
    actions = ['sortear_numero']

    def sortear_numero(self, request, queryset):
        if not queryset:
            self.message_user(request, "Nenhuma pessoa selecionada.")
            return
        
        # Seleciona aleatoriamente uma pessoa do queryset
        pessoa_sorteada = random.choice(queryset)
        
        # Mensagem de sucesso
        self.message_user(request, f'Número da sorte sorteado: {pessoa_sorteada.nome} - {pessoa_sorteada.numero_da_sorte} - Origem: {pessoa_sorteada.get_origem_display()}')

    sortear_numero.short_description = "Sortear um número da sorte"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sorteio/', self.admin_site.admin_view(self.sorteio_view), name='sorteio'),
        ]
        return custom_urls + urls

    def sorteio_view(self, request):
        # Aqui você pode implementar a lógica para exibir uma página de sorteio se necessário.
        # Por enquanto, vamos redirecionar para a lista de pessoas.
        self.message_user(request, "A página de sorteio ainda não foi implementada.")
        return redirect('admin:app_pessoa_changelist')  # Substitua 'app' pelo nome do seu aplicativo

admin.site.register(LuckyNumber, LuckyNumberAdmin)
