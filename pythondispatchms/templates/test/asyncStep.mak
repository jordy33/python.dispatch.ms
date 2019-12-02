%if cal=='1':
    <label for="startDate">Fecha de inicio *</label>
    <input id="startDate" name="startDate" type="datetime-local" class="required" value="${current_time}">
    <label for="endDate">Fecha de fin *</label>
    <input id="endDate" name="endDate" type="datetime-local" class="required" value="${current_time}">
%else:
            <table class="table">
                <thead>
                    <tr>
                        <th> DOW </th>
                    % for index in range(0,24):
                        <th>${ index }</th>
                    % endfor
                    </tr>
                </thead>
                % for item in ('Mon', 'Tue','Wed','Thr','Fri','Sat','Sun'):
                   <tr>
                      <th scope="row">${item}</th>

                        % for ndx in range(0,24):
                            <td>
                                <div class="checkbox">
                                        <label>
                                        <input name="Mon0" id="Mon0" type="checkbox" value="X" >
                                        <input type="hidden" name="Mon0" value="*" />
                                        </label>
                                </div>
                            </td>
                        % endfor
                  </tr>
                % endfor
            </table>
            </div>
                   <button>Guardar</button>
            </div>
            </form>
%endif


