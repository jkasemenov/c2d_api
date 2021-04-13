from pprint import pprint

from requests import get, post, put, delete


class Chat2DeskApi:
    API_URL = 'https://api.chat2desk.com'
    API_MODES_REQ = '/v1/help/api_modes'
    CHANNELS_REQ = '/v1/channels/'
    CLIENTS_REQ = '/v1/clients'
    COMPANIES_REQ = '/v1/companies'
    COUNTRIES_REQ = '/v1/countries'
    CUSTOM_CLIENT_FIELDS_REQ = '/v1/custom_client_fields'
    DELETE_OUTBOX_REQ = '/gateway/delete_outbox'
    DIALOG_STATES_REQ = '/v1/help/dialog_states'
    DIALOGS_REQ = '/v1/dialogs'
    MESSAGE_TYPES_REQ = '/v1/help/message_types'
    MESSAGES_REQ = '/v1/messages'
    OPERATORS_REQ = '/v1/operators'
    OPERATORS_GROUPS_REQ = '/v1/operators_groups'
    QR_DECODE_REQ = '/v1/qr-decode'
    REGIONS_REQ = '/v1/regions'
    REQUESTS_REQ = '/v1/requests'
    ROLES_REQ = '/v1/help/roles'
    SCENARIOS_GET_REQ = '/v1/scenarios/menu_items'
    SCENARIOS_REQ = '/v1/scenarios/send_menu_item'
    TAG_GROUPS_REQ = '/v1/tag_groups'
    TAGS_REQ = '/v1/tags'
    TAGS_ASSIGN_TO_REQ = '/v1/tags/assign_to'
    TEMPLATES_REQ = '/v1/templates'
    TRANSPORTS_REQ = '/v1/help/transports'
    WEB_ANALYTICS_DATA_REQ = '/v1/web_analytics_data'
    WEBHOOKS_REQ = '/v1/webhooks/'

    def __init__(self, access_token):
        self.access_token = access_token

    def api_modes_get(self):
        url = self.API_URL + self.API_MODES_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def channels_get(self, channel_id=None, phone=None, limit=None, offset=None):
        url = self.API_URL + self.CHANNELS_REQ
        params = {'phone': phone, 'limit': limit, 'offset': offset}
        if channel_id is not None:
            url = url + str(channel_id)
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def clients_get(self, client_id=None, transport=False, last_question=False, dialogs=False, questions=False,
                    phone=None, tags=None, created_after=None, order='asc', start_date=None, finish_date=None,
                    limit=None, offset=None):
        url = self.API_URL + self.CLIENTS_REQ
        params = {'phone': phone, 'tags': tags, 'order': order, 'limit': limit, 'offset': offset}
        if client_id is not None:
            url = url + '/' + str(client_id)
            if transport:
                url = url + '/transport'
            elif last_question:
                url = url + '/last_question'
            elif dialogs:
                url = url + '/dialogs'
            elif questions:
                url = url + '/questions'
                params['start_date'] = start_date
                params['finish_date'] = finish_date
        else:
            params['created_after'] = created_after
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def clients_post(self, phone, transport, channel_id, nickname=None):
        url = self.API_URL + self.CLIENTS_REQ
        params = {'phone': phone, 'transport': transport, 'channel_id': channel_id, 'nickname': nickname}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def clients_put(self, client_id, nickname=None, custom_fields=None, external_id=None, external_service=None):
        url = self.API_URL + self.CLIENTS_REQ + '/' + str(client_id)
        params = {'nickname': nickname, 'custom fields': custom_fields, 'external_id': external_id,
                  'external_service': external_service}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def companies_api_info_get(self):
        url = self.API_URL + self.COMPANIES_REQ + '/api_info'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def companies_put(self, custom_fields):
        url = self.API_URL + self.COMPANIES_REQ
        params = {'custom_fields': custom_fields}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def companies_switch_mode_put(self, mode):
        url = self.API_URL + self.COMPANIES_REQ + '/switch_mode'
        params = {'mode': mode}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def countries_get(self, limit=None, offset=None):
        url = self.API_URL + self.COUNTRIES_REQ
        params = {'limit': limit, 'offset': offset}
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def custom_client_fields_get(self):
        url = self.API_URL + self.CUSTOM_CLIENT_FIELDS_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def delete_outbox_get(self):
        url = self.API_URL + self.DELETE_OUTBOX_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def dialog_states_get(self):
        url = self.API_URL + self.DIALOG_STATES_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def dialogs_get(self, dialog_id=None, unanswered=False, operator_id=None, state=None, order='asc',
                    limit=None, offset=None):
        url = self.API_URL + self.DIALOGS_REQ
        params = {'operator_id': operator_id, 'state': state, 'order': order, 'limit': limit, 'offset': offset}
        if dialog_id is not None:
            url = url + '/' + str(dialog_id)
        elif unanswered:
            url = url + '/unanswered'
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def dialogs_put(self, dialog_id, operator_id=None, state=None):
        url = self.API_URL + self.DIALOGS_REQ + '/' + str(dialog_id)
        params = {'operator_id': operator_id, 'state': state}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def message_types_get(self):
        url = self.API_URL + self.MESSAGE_TYPES_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def messages_get(self, message_id=None, transport=None, channel_id=None, client_id=None, type=None, dialog_id=None,
                     read=None, order='asc', start_date=None, finish_date=None, operator_id=None,
                     start_id=None, limit=None):
        url = self.API_URL + self.MESSAGES_REQ
        params = {'transport': transport, 'channel_id': channel_id, 'client_id': client_id, 'type': type,
                  'dialog_id': dialog_id, 'read': read, 'order': order, 'start_date': start_date,
                  'finish_date': finish_date, 'operator_id': operator_id, 'start_id': start_id, 'limit': limit}
        if message_id is not None:
            url = url + '/' + str(message_id)
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def messages_post(self, client_id, text, attachment=None, pdf=None, type='to_client', transport=None,
                      channel_id=None, operator_id=None, open_dialog=True, encrypted=False, external_id=None):
        url = self.API_URL + self.MESSAGES_REQ
        params = {'client_id': client_id, 'text': text, 'attachment': attachment, 'pdf': pdf, 'type': type,
                  'transport': transport, 'channel_id': channel_id, 'operator_id': operator_id,
                  'open_dialog': open_dialog, 'encrypted': encrypted, 'external_id': external_id}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def messages_with_buttons_post(self):
        return

    def messages_id_transfer_get(self, message_id, operator_id):
        url = self.API_URL + self.MESSAGES_REQ + f'/{message_id}/transfer'
        params = {'operator_id': operator_id}
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    # def messages_inbox_post(self):
    #     return

    def messages_read_get(self, message_id, read=True):
        url = self.API_URL + self.MESSAGES_REQ + f'/{message_id}/{"read" if read else "unread"}'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def operators_get(self, statuses=False, phone=None, email=None, online=None, status_id=None):
        url = self.API_URL + self.OPERATORS_REQ
        params = {'phone': phone, 'email': email, 'online': online, 'status_id': status_id}
        if statuses:
            url = url + '/statuses'
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def operators_put(self, operator_id, status_id):
        url = self.API_URL + self.OPERATORS_REQ + f'/statuses/{operator_id}'
        params = {'status_id': status_id}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def operators_groups_get(self):
        url = self.API_URL + self.OPERATORS_GROUPS_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def qr_decode_post(self, image_path):
        url = self.API_URL + self.QR_DECODE_REQ
        params = {'image_path': image_path}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def regions_get(self):
        url = self.API_URL + self.REGIONS_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def requests_get(self, request_id, messages=False):
        url = self.API_URL + self.REQUESTS_REQ + f'/{request_id}{"/messages" if messages else ""}'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def requests_close_put(self, request_id=None, client_id=None):
        url = self.API_URL + self.REQUESTS_REQ + '/close'
        params = {'request_id': request_id, 'client_id': client_id}
        response = put(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def roles_get(self):
        url = self.API_URL + self.ROLES_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def scenarios_get(self, channel_id=None, level=None):
        url = self.API_URL + self.SCENARIOS_GET_REQ
        params = {'channel_id': channel_id, 'level': level}
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def scenarios_post(self, client_id, menu_item_id=None):
        url = self.API_URL + self.SCENARIOS_REQ
        params = {'client_id': client_id, 'menu_item_id': menu_item_id}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    # def statistics_get(self):
    #     return

    def tag_groups_post(self, tag_group_name, order_show=1, display=1):
        url = self.API_URL + self.TAG_GROUPS_REQ
        params = {'tag_group_name': tag_group_name, 'order_show': order_show, 'display': display}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def tags_delete(self, tag_id, client_id=None, request_id=None):
        url = self.API_URL + self.TAGS_REQ + f'/{tag_id}/delete_from'
        params = {'client_id': client_id, 'request_id': request_id}
        response = delete(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def tags_get(self, tag_id=None):
        url = self.API_URL + self.TAGS_REQ
        if tag_id is not None:
            url = url + f'/{tag_id}'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def tags_post(self, tag_group_id, tag_label, tag_description, tag_bg_color='000000', tag_text_color='ffffff',
                  order_show=1):
        url = self.API_URL + self.TAGS_REQ
        params = {'tag_group_id': tag_group_id, 'tag_label': tag_label, 'tag_description': tag_description,
                  'tag_bg_color': tag_bg_color, 'tag_text_color': tag_text_color, 'order_show': order_show}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def tags_assign_to_post(self, tag_ids, assignee_type, assignee_id):
        url = self.API_URL + self.TAGS_ASSIGN_TO_REQ
        params = {'tag_ids': tag_ids, 'assignee_type': assignee_type, 'assignee_id': assignee_id}
        response = post(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def templates_get(self, template_id=None):
        url = self.API_URL + self.TEMPLATES_REQ
        if template_id is not None:
            url = url + f'/{template_id}'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def transfer_to_group_get(self, message_id, group_id):
        url = self.API_URL + self.MESSAGES_REQ + f'/{message_id}/transfer_to_group'
        params = {'group_id': group_id}
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def transports_get(self):
        url = self.API_URL + self.TRANSPORTS_REQ
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def web_analytics_data_get(self, date_from=None, date_to=None, order='asc', client_id=None,
                               limit=None, offset=None):
        url = self.API_URL + self.WEB_ANALYTICS_DATA_REQ
        params = {'date_from': date_from, 'date_to': date_to, 'order': order, 'client_id': client_id, 'limit': limit,
                  'offset': offset}
        response = get(url=url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    def webhooks_delete(self, webhook_id):
        url = self.API_URL + self.WEBHOOKS_REQ + f'/{webhook_id}'
        response = delete(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def webhooks_get(self, webhook_id=None):
        url = self.API_URL + self.WEBHOOKS_REQ
        if webhook_id is not None:
            url = url + f'/{webhook_id}'
        response = get(url=url, headers={'Authorization': self.access_token})
        return response.json()

    def webhooks_post(self, url, name, events):
        _url = self.API_URL + self.WEBHOOKS_REQ
        params = {'url': url, 'name': name, 'events': events}
        response = post(url=_url, params=params, headers={'Authorization': self.access_token})
        return response.json()

    # def web_hook_post(self):
    #     return

    def webhooks_put(self, webhook_id, url, name, events, status=None):
        _url = self.API_URL + self.WEBHOOKS_REQ + f'/{webhook_id}'
        params = {'url': url, 'name': name, 'events': events, 'status': status}
        response = put(url=_url, params=params, headers={'Authorization': self.access_token})
        return response.json()
