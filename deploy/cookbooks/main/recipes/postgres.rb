package "postgresql" do
    :upgrade
end

service "postgresql" do
  enabled true
  running true
  supports :status => true, :restart => true
  action [:enable, :start]
end

cookbook_file "/etc/postgresql/9.1/main/pg_hba.conf" do
    source "pg_hba.conf"
    mode 0755
    notifies :restart, resources(:service => "postgresql")
end
