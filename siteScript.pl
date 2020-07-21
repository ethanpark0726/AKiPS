sub web_export_device_list
{
   my %ip_data;
   my @device = ();
   for my $line (adb_result ('mget text * sys ip4addr')) {
      my ($dev, undef, undef, undef, $val) = split (" ", $line, 5);
      push @device, $dev;
      $ip_data{$dev} = $val;
   }

   # deviceName,ip4 address
   for my $dev (@device) {
      printf "%s, %s\n", $dev, $ip_data{$dev};
   }
   return;
}
